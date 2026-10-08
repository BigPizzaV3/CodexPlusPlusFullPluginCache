"use client";

import { useEffect, useMemo, useRef, useState } from "react";
import { planImages, fixtures, type Fixture, type FloorId, type SystemId } from "./fixtures";

const statuses = { "not-started": "Not Started", "roughed-in": "Roughed In", "finish-installed": "Finish Installed", complete: "Complete", issue: "Issue / Blocked" } as const;
const systemLabels: Record<SystemId, string> = { power: "Power" };
function floorLabel(system: SystemId, floor: FloorId) { return planImages[system]?.[floor]?.label || floor; }
type Status = keyof typeof statuses;
type Saved = Record<string, { status: Status; updatedAt?: string }>;
type HistoryRow = { id: number; fixtureId: string; previousStatus: Status; newStatus: Status; changedAt: string };
type Note = { id: number; content: string; system: SystemId | null; floor: FloorId | null; createdAt: string; updatedAt: string };
type Manager = { email: string; addedBy: string; createdAt: string };
type ReportGroup = { system: string; floor: string; deviceType: string; status: string; count: number };
type ReportNote = Note & { systemLabel: string; floorLabel: string | null };
type ProgressReport = { id: number; periodType: "today" | "week" | "since-last"; periodStart: string; periodEnd: string; createdAt: string; createdBy: string; summary: { groups: ReportGroup[]; notes: ReportNote[]; deviceCount: number; noteCount: number; daysSincePrevious: number | null } };
const backupKey = "electrical-progress-tracker-v3";

function localTime(value?: string) {
  if (!value) return "No recorded change";
  const normalized = value.includes("T") ? value : `${value.replace(" ", "T")}Z`;
  const date = new Date(normalized);
  return Number.isNaN(date.getTime()) ? value : date.toLocaleString([], { dateStyle: "medium", timeStyle: "short" });
}

export function Tracker({ readOnly = false, isOwner = false, managerEmail = "" }: { readOnly?: boolean; isOwner?: boolean; managerEmail?: string }) {
  const [saved, setSaved] = useState<Saved>({});
  const [activeSystem, setActiveSystem] = useState<SystemId>("power");
  const [activeFloor, setActiveFloor] = useState<FloorId>("first");
  const [activeType, setActiveType] = useState("all");
  const [activeStatus, setActiveStatus] = useState("all");
  const [selected, setSelected] = useState<Fixture | null>(null);
  const [history, setHistory] = useState<HistoryRow[]>([]);
  const [bulkMode, setBulkMode] = useState(false);
  const [selectedIds, setSelectedIds] = useState<Set<string>>(new Set());
  const [view, setView] = useState<"tracker" | "notes" | "reports" | "settings">("tracker");
  const [notes, setNotes] = useState<Note[]>([]);
  const [noteDraft, setNoteDraft] = useState("");
  const [editingNote, setEditingNote] = useState<number | null>(null);
  const [editDraft, setEditDraft] = useState("");
  const [managers, setManagers] = useState<Manager[]>([]);
  const [ownerEmail, setOwnerEmail] = useState("");
  const [managerDraft, setManagerDraft] = useState("");
  const [settingsMessage, setSettingsMessage] = useState("");
  const [reports, setReports] = useState<ProgressReport[]>([]);
  const [reportPeriod, setReportPeriod] = useState<"today" | "week" | "since-last">("since-last");
  const [reportMessage, setReportMessage] = useState("");
  const [generatingReport, setGeneratingReport] = useState(false);
  const [zoom, setZoom] = useState(1);
  const [sync, setSync] = useState<"loading" | "saved" | "saving" | "offline">("loading");
  const viewport = useRef<HTMLDivElement>(null);

  async function saveUpdates(updates: Array<{ fixtureId: string; status: Status }>) {
    if (!updates.length) return { saved: 0 };
    const now = new Date().toISOString();
    setSaved(current => {
      const next = { ...current };
      updates.forEach(({ fixtureId, status }) => { next[fixtureId] = { status, updatedAt: now }; });
      localStorage.setItem(backupKey, JSON.stringify(next));
      return next;
    });
    setSync("saving");
    try {
      let savedCount = 0;
      for (let i = 0; i < updates.length; i += 50) {
        const chunk = updates.slice(i, i + 50);
        const response = await fetch("/api/progress", { method: "POST", headers: { "content-type": "application/json" }, body: JSON.stringify({ updates: chunk }) });
        if (!response.ok) throw new Error("Progress could not be saved");
        const data = await response.json() as { saved: number; progress?: Array<{ fixtureId: string; status: Status; updatedAt: string }> };
        savedCount += data.saved;
        if (data.progress?.length) setSaved(current => {
          const next = { ...current };
          data.progress!.forEach(row => { next[row.fixtureId] = { status: row.status, updatedAt: row.updatedAt }; });
          localStorage.setItem(backupKey, JSON.stringify(next));
          return next;
        });
      }
      setSync("saved");
      return { saved: savedCount };
    } catch (error) { setSync("offline"); throw error; }
  }

  async function loadNotes() {
    try {
      const response = await fetch("/api/notes", { cache: "no-store" });
      if (!response.ok) throw new Error();
      const data = await response.json() as { notes: Note[] };
      setNotes(data.notes);
    } catch { setSync("offline"); }
  }

  async function loadManagers() {
    if (!isOwner) return;
    const response = await fetch("/api/managers", { cache: "no-store" });
    if (!response.ok) return;
    const data = await response.json() as { ownerEmail: string; managers: Manager[] };
    setOwnerEmail(data.ownerEmail); setManagers(data.managers);
  }

  async function loadReports() {
    try {
      const response = await fetch("/api/reports", { cache: "no-store" });
      if (!response.ok) throw new Error();
      const data = await response.json() as { reports: ProgressReport[] };
      setReports(data.reports);
    } catch { setReportMessage("Progress reports are temporarily unavailable."); }
  }

  useEffect(() => {
    let cancelled = false;
    async function load() {
      let local: Saved = {};
      if (!readOnly) try { local = JSON.parse(localStorage.getItem(backupKey) || "{}"); } catch {}
      try {
        const response = await fetch("/api/progress", { cache: "no-store" });
        if (!response.ok) throw new Error();
        const data = await response.json() as { progress: Array<{ fixtureId: string; status: Status; updatedAt: string }> };
        const remote: Saved = Object.fromEntries(data.progress.map(row => [row.fixtureId, { status: row.status, updatedAt: row.updatedAt }]));
        const missingLocal = readOnly ? [] : Object.entries(local).filter(([id, value]) => !remote[id] && value.status !== "not-started");
        const merged = { ...local, ...remote };
        if (!cancelled) { setSaved(merged); if (!readOnly) localStorage.setItem(backupKey, JSON.stringify(merged)); setSync("saved"); }
        if (missingLocal.length) await saveUpdates(missingLocal.map(([fixtureId, value]) => ({ fixtureId, status: value.status })));
      } catch { if (!cancelled) { setSaved(local); setSync("offline"); } }
    }
    void load(); void loadNotes(); void loadManagers();
    return () => { cancelled = true; };
  }, [readOnly]);

  useEffect(() => {
    if (!selected) { setHistory([]); return; }
    let cancelled = false;
    fetch(`/api/history?fixtureId=${encodeURIComponent(selected.id)}`, { cache: "no-store" })
      .then(response => response.ok ? response.json() : Promise.reject())
      .then((data: { history: HistoryRow[] }) => { if (!cancelled) setHistory(data.history); })
      .catch(() => { if (!cancelled) setHistory([]); });
    return () => { cancelled = true; };
  }, [selected, saved[selected?.id || ""]?.updatedAt]);

  useEffect(() => {
    if (readOnly) return;
    const modelContext = (document as Document & { modelContext?: { registerTool: (tool: unknown, options?: { signal?: AbortSignal }) => void | Promise<void> } }).modelContext;
    if (!modelContext?.registerTool) return;
    const lifecycle = new AbortController();
    void Promise.resolve(modelContext.registerTool({
      name: "update_electrical_device_statuses", title: "Update electrical device statuses",
      description: "Update one or more mapped electrical devices and save timestamped status history.",
      inputSchema: { type: "object", properties: { updates: { type: "array", minItems: 1, maxItems: fixtures.length, items: { type: "object", properties: { deviceId: { type: "string" }, status: { type: "string", enum: Object.keys(statuses) } }, required: ["deviceId", "status"], additionalProperties: false } } }, required: ["updates"], additionalProperties: false },
      annotations: { readOnlyHint: false, untrustedContentHint: false },
      async execute(input: unknown) {
        const candidate = input as { updates?: Array<{ deviceId?: string; status?: string }> };
        const known = new Set(fixtures.map(f => f.id));
        const updates = candidate.updates?.map(item => ({ fixtureId: item.deviceId || "", status: item.status as Status })) || [];
        if (!updates.length || updates.some(item => !known.has(item.fixtureId) || !(item.status in statuses))) throw new Error("A valid device ID and status are required");
        return saveUpdates(updates);
      },
    }, { signal: lifecycle.signal })).catch(() => {});
    return () => lifecycle.abort();
  }, [readOnly, saved]);

  const floorFixtures = useMemo(() => fixtures.filter(f => f.floor === activeFloor && f.system === activeSystem), [activeFloor, activeSystem]);
  const types = useMemo(() => { const counts = new Map<string, number>(); floorFixtures.forEach(f => counts.set(f.type, (counts.get(f.type) || 0) + 1)); return [...counts.entries()].sort(([a], [b]) => a.localeCompare(b)); }, [floorFixtures]);
  const statusOf = (id: string): Status => saved[id]?.status || "not-started";
  const visibleFixtures = floorFixtures.filter(f => (activeType === "all" || f.type === activeType) && (activeStatus === "all" || statusOf(f.id) === activeStatus));
  const complete = floorFixtures.filter(f => statusOf(f.id) === "complete").length;
  const rough = floorFixtures.filter(f => statusOf(f.id) === "roughed-in").length;
  const finish = floorFixtures.filter(f => statusOf(f.id) === "finish-installed").length;
  const percent = floorFixtures.length ? Math.round(((complete + finish) / floorFixtures.length) * 100) : 0;
  const systemFixtures = fixtures.filter(f => f.system === activeSystem);
  const overallPercent = systemFixtures.length ? Math.round((systemFixtures.filter(f => ["complete", "finish-installed"].includes(statusOf(f.id))).length / systemFixtures.length) * 100) : 0;
  const currentPlan = planImages[activeSystem][activeFloor]!;

  function resetSelection() { setBulkMode(false); setSelectedIds(new Set()); }
  function chooseSystem(system: SystemId) { const nextFloor = planImages[system][activeFloor] ? activeFloor : (Object.keys(planImages[system])[0] as FloorId); setActiveSystem(system); setActiveFloor(nextFloor); setActiveType("all"); setActiveStatus("all"); setSelected(null); resetSelection(); setZoom(1); viewport.current?.scrollTo({ left: 0, top: 0 }); }
  function chooseFloor(floor: FloorId) { setActiveFloor(floor); setActiveType("all"); setActiveStatus("all"); setSelected(null); resetSelection(); setZoom(1); viewport.current?.scrollTo({ left: 0, top: 0 }); }
  function markerClick(fixture: Fixture) { if (bulkMode && !readOnly) setSelectedIds(current => { const next = new Set(current); next.has(fixture.id) ? next.delete(fixture.id) : next.add(fixture.id); return next; }); else setSelected(fixture); }
  async function applyBulk(status: Status) { try { await saveUpdates([...selectedIds].map(fixtureId => ({ fixtureId, status }))); resetSelection(); } catch {} }
  async function updateStatus(status: Status) { if (!selected) return; try { await saveUpdates([{ fixtureId: selected.id, status }]); } catch {} }
  function fit() { setZoom(Math.max(.45, ((viewport.current?.clientWidth || 1500) - 18) / 1500)); viewport.current?.scrollTo({ left: 0, top: 0, behavior: "smooth" }); }

  async function addNote() {
    const content = noteDraft.trim(); if (!content) return; setSync("saving");
    const response = await fetch("/api/notes", { method: "POST", headers: { "content-type": "application/json" }, body: JSON.stringify({ content, system: activeSystem, floor: activeFloor }) });
    if (!response.ok) { setSync("offline"); return; }
    const data = await response.json() as { note: Note }; setNotes(current => [data.note, ...current]); setNoteDraft(""); setSync("saved");
  }
  async function saveNote(id: number) {
    const content = editDraft.trim(); if (!content) return;
    const response = await fetch("/api/notes", { method: "PATCH", headers: { "content-type": "application/json" }, body: JSON.stringify({ id, content }) });
    if (!response.ok) { setSync("offline"); return; }
    const data = await response.json() as { note: Note }; setNotes(current => current.map(note => note.id === id ? data.note : note)); setEditingNote(null); setSync("saved");
  }
  async function deleteNote(id: number) { const response = await fetch("/api/notes", { method: "DELETE", headers: { "content-type": "application/json" }, body: JSON.stringify({ id }) }); if (!response.ok) { setSync("offline"); return; } setNotes(current => current.filter(note => note.id !== id)); }

  async function clearHistory(fixtureId?: string) {
    const label = fixtureId ? `the recorded status history for ${fixtureId}` : "all recorded device status history";
    if (!window.confirm(`Clear ${label}? Current device statuses will not change. This cannot be undone.`)) return;
    const response = await fetch("/api/history", { method: "DELETE", headers: { "content-type": "application/json" }, body: JSON.stringify(fixtureId ? { fixtureId } : { all: true }) });
    if (!response.ok) { setSettingsMessage("History could not be cleared."); return; }
    if (fixtureId) {
      setHistory([]);
      setSaved(current => ({ ...current, [fixtureId]: { ...current[fixtureId], updatedAt: undefined } }));
    } else {
      setSaved(current => Object.fromEntries(Object.entries(current).map(([id, value]) => [id, { ...value, updatedAt: undefined }])));
      setHistory([]);
      setSettingsMessage("All device status history has been cleared. Current statuses were preserved.");
    }
  }

  async function addManager() {
    const email = managerDraft.trim().toLowerCase(); if (!email) return;
    const response = await fetch("/api/managers", { method: "POST", headers: { "content-type": "application/json" }, body: JSON.stringify({ email }) });
    const data = await response.json() as { manager?: Manager; error?: string };
    if (!response.ok || !data.manager) { setSettingsMessage(data.error || "Manager could not be added."); return; }
    setManagers(current => [...current.filter(manager => manager.email !== data.manager!.email), data.manager!].sort((a, b) => a.email.localeCompare(b.email)));
    setManagerDraft(""); setSettingsMessage(`${data.manager.email} can now use manager mode.`);
  }

  async function removeManager(email: string) {
    if (!window.confirm(`Remove manager access for ${email}?`)) return;
    const response = await fetch("/api/managers", { method: "DELETE", headers: { "content-type": "application/json" }, body: JSON.stringify({ email }) });
    if (!response.ok) { setSettingsMessage("Manager access could not be removed."); return; }
    setManagers(current => current.filter(manager => manager.email !== email));
    setSettingsMessage(`${email} no longer has manager access.`);
  }

  async function generateReport() {
    const now = new Date();
    let start: Date;
    if (reportPeriod === "today") start = new Date(now.getFullYear(), now.getMonth(), now.getDate());
    else if (reportPeriod === "week") {
      start = new Date(now.getFullYear(), now.getMonth(), now.getDate());
      const day = start.getDay();
      start.setDate(start.getDate() - (day === 0 ? 6 : day - 1));
    } else if (reports.length) start = new Date(reports[0].createdAt.includes("T") ? reports[0].createdAt : `${reports[0].createdAt.replace(" ", "T")}Z`);
    else {
      start = new Date(now.getFullYear(), now.getMonth(), now.getDate());
      const day = start.getDay();
      start.setDate(start.getDate() - (day === 0 ? 6 : day - 1));
    }
    setGeneratingReport(true); setReportMessage("");
    try {
      const response = await fetch("/api/reports", { method: "POST", headers: { "content-type": "application/json" }, body: JSON.stringify({ periodType: reportPeriod, periodStart: start.toISOString(), periodEnd: now.toISOString() }) });
      const data = await response.json() as { report?: ProgressReport; error?: string };
      if (!response.ok || !data.report) { setReportMessage(data.error || "Report could not be generated."); return; }
      setReports(current => [data.report!, ...current]); setReportMessage("Progress report finalized and saved.");
    } catch { setReportMessage("Report could not be generated."); }
    finally { setGeneratingReport(false); }
  }

  function reportRange(report: ProgressReport) {
    return `${new Date(report.periodStart).toLocaleDateString([], { dateStyle: "medium" })} – ${new Date(report.periodEnd).toLocaleDateString([], { dateStyle: "medium" })}`;
  }

  return <main>
    <header className="topbar"><div><p className="eyebrow">PROJECT ELECTRICAL PROGRESS</p><h1>{view === "tracker" ? `${currentPlan.label} ${systemLabels[activeSystem]} Progress` : view === "notes" ? "Project Notes" : view === "reports" ? "Progress Reports" : "Manager Settings"}</h1></div><nav className="view-tabs" aria-label="Tracker sections"><button className={view === "tracker" ? "active" : ""} onClick={() => setView("tracker")}>Tracker</button><button className={view === "notes" ? "active" : ""} onClick={() => { setView("notes"); void loadNotes(); }}>Notes</button><button className={view === "reports" ? "active" : ""} onClick={() => { setView("reports"); void loadReports(); }}>Reports</button>{!readOnly && <button className={view === "settings" ? "active" : ""} onClick={() => { setView("settings"); void loadManagers(); }}>Settings</button>}</nav><div className="top-actions"><span className={`sync ${sync}`}>{readOnly ? (sync === "loading" ? "Loading" : sync === "offline" ? "Unavailable" : "VIEW ONLY") : (sync === "loading" ? "Loading" : sync === "saving" ? "Saving" : sync === "offline" ? "Not synced" : "Saved")}</span>{view === "tracker" && <><button className="icon-button" aria-label="Zoom out" onClick={() => setZoom(Math.max(.45, zoom - .15))}>−</button><span>{Math.round(zoom * 100)}%</span><button className="icon-button" aria-label="Zoom in" onClick={() => setZoom(Math.min(2.2, zoom + .15))}>+</button><button className="button secondary" onClick={fit}>Fit drawing</button></>}</div></header>
    {view === "reports" ? <section className="reports-view">
      {!readOnly && <section className="report-generator"><div><p className="eyebrow">NEW SNAPSHOT</p><h2>Generate progress report</h2><p>Counts each device once using its final status during the selected period, and includes project notes from the same dates.</p></div><div className="report-controls"><label>Report period<select value={reportPeriod} onChange={event => setReportPeriod(event.target.value as typeof reportPeriod)}><option value="since-last">Since last report</option><option value="today">Today</option><option value="week">This week</option></select></label><button className="button primary" onClick={generateReport} disabled={generatingReport}>{generatingReport ? "Generating…" : "Generate report"}</button></div>{reportMessage && <p className="report-message">{reportMessage}</p>}</section>}
      <div className="reports-list">{reports.length ? reports.map(report => <article className="report-card" key={report.id}><header><div><p className="eyebrow">FINALIZED PROGRESS REPORT</p><h2>{reportRange(report)}</h2></div><span>{report.summary.deviceCount} device{report.summary.deviceCount === 1 ? "" : "s"} · {report.summary.noteCount} note{report.summary.noteCount === 1 ? "" : "s"}</span></header><p className="report-baseline">{report.summary.daysSincePrevious === null ? "First generated progress report" : `Generated ${report.summary.daysSincePrevious} day${report.summary.daysSincePrevious === 1 ? "" : "s"} after the previous report`} · {localTime(report.createdAt)}</p><div className="report-groups">{report.summary.groups.map((group, index) => <p key={`${group.system}-${group.floor}-${group.deviceType}-${group.status}-${index}`}><strong>{group.count}</strong> {group.deviceType} device{group.count === 1 ? " was" : "s were"} marked <strong>{group.status}</strong> · {group.floor} {group.system}</p>)}</div>{report.summary.notes.length > 0 && <div className="report-notes"><h3>Project notes</h3>{report.summary.notes.map(note => <div key={note.id}><p>{note.content}</p><small>{note.systemLabel}{note.floorLabel ? ` · ${note.floorLabel}` : ""} · {localTime(note.updatedAt)}</small></div>)}</div>}<footer>Finalized by {report.createdBy}</footer></article>) : <div className="empty-state"><h2>No finalized reports yet</h2><p>{readOnly ? "Finalized progress reports will appear here." : "Choose a period above to create the first permanent report snapshot."}</p></div>}</div>
    </section> : view === "settings" ? <section className="settings-view">
      <div className="settings-grid">
        <section className="settings-card danger-zone"><p className="eyebrow">STATUS RECORDS</p><h2>Clear timestamp history</h2><p>Remove every recorded device status timestamp while keeping each device's current status unchanged.</p><button className="danger-button" onClick={() => clearHistory()}>Clear all status history</button></section>
        <section className="settings-card"><p className="eyebrow">SIGNED IN</p><h2>{managerEmail}</h2><p>You have manager access to status changes, bulk updates, notes, and history controls.</p></section>
        {isOwner && <section className="settings-card manager-card"><p className="eyebrow">OWNER CONTROL</p><h2>Project managers</h2><p>Add the exact email address a coworker uses for their personal ChatGPT account.</p><div className="manager-form"><input type="email" value={managerDraft} onChange={e => setManagerDraft(e.target.value)} placeholder="coworker@example.com"/><button className="button primary" onClick={addManager} disabled={!managerDraft.trim()}>Add manager</button></div><div className="manager-list"><div><span><strong>{ownerEmail || managerEmail}</strong><small>Owner</small></span></div>{managers.map(manager => <div key={manager.email}><span><strong>{manager.email}</strong><small>Manager · added {localTime(manager.createdAt)}</small></span><button onClick={() => removeManager(manager.email)}>Remove</button></div>)}</div></section>}
        {settingsMessage && <p className="settings-message">{settingsMessage}</p>}
      </div>
    </section> : view === "notes" ? <section className="notes-view">{!readOnly && <div className="note-composer"><label htmlFor="note-draft">New project note</label><textarea id="note-draft" value={noteDraft} onChange={e => setNoteDraft(e.target.value)} placeholder="Example: Light fixture finish installation delayed due to missing ceiling grid." maxLength={4000}/><div><span>Tagged to {systemLabels[activeSystem]} · {floorLabel(activeSystem, activeFloor)}</span><button className="button primary" onClick={addNote} disabled={!noteDraft.trim()}>Add note</button></div></div>}<div className="notes-list">{notes.length ? notes.map(note => <article className="note-card" key={note.id}><div className="note-meta"><span>{note.system ? systemLabels[note.system] : "General"}{note.floor ? ` · ${note.system ? floorLabel(note.system, note.floor) : note.floor}` : ""}</span><time>{localTime(note.updatedAt)}</time></div>{editingNote === note.id ? <><textarea value={editDraft} onChange={e => setEditDraft(e.target.value)} maxLength={4000}/><div className="note-actions"><button onClick={() => setEditingNote(null)}>Cancel</button><button className="save-note" onClick={() => saveNote(note.id)}>Save changes</button></div></> : <><p>{note.content}</p><small>Created {localTime(note.createdAt)}{note.updatedAt !== note.createdAt ? ` · Edited ${localTime(note.updatedAt)}` : ""}</small>{!readOnly && <div className="note-actions"><button onClick={() => { setEditingNote(note.id); setEditDraft(note.content); }}>Edit</button><button className="delete-note" onClick={() => deleteNote(note.id)}>Delete</button></div>}</>}</article>) : <div className="empty-state"><h2>No project notes yet</h2><p>{readOnly ? "Project notes will appear here when they are added." : "Add the first field note above."}</p></div>}</div></section> : <>
      <div className="selector-bar"><nav className="system-nav" aria-label="Select system">{(Object.keys(planImages) as SystemId[]).map(system => <button key={system} className={activeSystem === system ? "active" : ""} onClick={() => chooseSystem(system)}>{systemLabels[system]}</button>)}</nav><nav className="floor-nav" aria-label="Select floor">{(Object.entries(planImages[activeSystem]) as Array<[FloorId, { label: string; image: string }]>).map(([floor, plan]) => { const count = fixtures.filter(f => f.floor === floor && f.system === activeSystem).length; return <button key={floor} className={activeFloor === floor ? "active" : ""} onClick={() => chooseFloor(floor)}><strong>{plan.label}</strong><span>{count} devices</span></button>; })}</nav></div>
      <section className="summary" aria-label="Progress summary"><div className="progress-copy"><span>{percent}%</span><small>finish complete</small></div><div className="progress-track"><div style={{ width: `${percent}%` }} /></div><div className="counts"><span><strong>{complete}</strong> complete</span><span><strong>{rough}</strong> roughed in</span><span><strong>{floorFixtures.length}</strong> mapped</span><span className="overall"><strong>{overallPercent}%</strong> overall {systemLabels[activeSystem]}</span></div></section>
      <div className="workspace"><aside className="sidebar"><div className="panel-heading"><h2>Device Filters</h2><button className="text-button" onClick={() => { setActiveType("all"); setActiveStatus("all"); }}>Show all</button></div><div className="filter-list"><button className={activeType === "all" ? "active" : ""} onClick={() => setActiveType("all")}><span>All devices</span><span className="count">{floorFixtures.length}</span></button>{types.map(([type, count]) => <button key={type} className={activeType === type ? "active" : ""} onClick={() => setActiveType(type)}><span>{type}</span><span className="count">{count}</span></button>)}</div><div className="legend"><h2>Status</h2>{Object.entries(statuses).map(([key, label]) => <button key={key} className={activeStatus === key ? "active" : ""} onClick={() => setActiveStatus(activeStatus === key ? "all" : key)}><i className={`dot ${key}`} />{label}</button>)}</div><p className="prototype-note">{floorFixtures.length} mapped {systemLabels[activeSystem]} devices across {types.length} types on the {currentPlan.label.toLowerCase()}. {readOnly ? "Select a marker to view its status history." : "Status changes and notes are timestamped automatically."}</p></aside>
        <section className="drawing-shell" aria-label="Interactive drawing">{!readOnly && <div className="bulk-controls"><button className={bulkMode ? "active" : ""} onClick={() => bulkMode ? resetSelection() : setBulkMode(true)}>{bulkMode ? "Cancel selection" : "Select multiple"}</button>{bulkMode && <><button onClick={() => setSelectedIds(new Set(visibleFixtures.map(f => f.id)))}>Select all shown</button><span>{selectedIds.size} selected</span>{selectedIds.size > 0 && <div className="bulk-statuses">{Object.entries(statuses).map(([key, label]) => <button key={key} onClick={() => applyBulk(key as Status)}><i className={`dot ${key}`} />{label}</button>)}</div>}</>}</div>}<div ref={viewport} className="drawing-viewport"><div className="drawing-stage" style={{ width: `${1500 * zoom}px` }}><img src={currentPlan.image} alt={`${currentPlan.label} ${systemLabels[activeSystem]} plan`} draggable={false}/><div className="marker-layer">{floorFixtures.map(f => { const status = statusOf(f.id); const hidden = !visibleFixtures.includes(f); return <button key={f.id} className={`marker${hidden ? " hidden" : ""}${selectedIds.has(f.id) ? " selected-marker" : ""}`} data-status={status} style={{ left: `${f.x}%`, top: `${f.y}%` }} aria-label={`${f.id}: ${statuses[status]}`} title={`${f.id} - ${statuses[status]}${saved[f.id]?.updatedAt ? ` - ${localTime(saved[f.id].updatedAt)}` : ""}`} onClick={() => markerClick(f)} />; })}</div></div></div></section></div>
    </>}
    {selected && <div className="dialog-backdrop" role="presentation" onMouseDown={() => setSelected(null)}><section className="dialog-card" role="dialog" aria-modal="true" aria-labelledby="fixture-title" onMouseDown={e => e.stopPropagation()}><div className="dialog-header"><div><p className="eyebrow">SELECTED DEVICE</p><h2 id="fixture-title">{selected.id}</h2></div><button className="close-button" aria-label="Close" onClick={() => setSelected(null)}>×</button></div><p className="fixture-meta">{selected.type} · {statuses[statusOf(selected.id)]}</p><p className="last-change"><strong>Last changed</strong><span>{localTime(saved[selected.id]?.updatedAt)}</span></p>{!readOnly && <fieldset><legend>Update status</legend>{Object.entries(statuses).map(([key, label]) => <button key={key} type="button" className={statusOf(selected.id) === key ? "current" : ""} onClick={() => updateStatus(key as Status)}><i className={`dot ${key}`} />{label}</button>)}</fieldset>}<div className="history"><div className="history-heading"><h3>Status history</h3>{!readOnly && <button className="clear-history" onClick={() => clearHistory(selected.id)}>Clear history</button>}</div>{history.length ? history.map(row => <div key={row.id}><span><i className={`dot ${row.newStatus}`} />{statuses[row.previousStatus]} → {statuses[row.newStatus]}</span><time>{localTime(row.changedAt)}</time></div>) : <p>No recorded status changes yet.</p>}</div></section></div>}
  </main>;
}

export default function Home() { return <Tracker readOnly />; }
