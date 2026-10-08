# EvO — evoluční operátor přípustných stavů nad aktuální realitou

## Kanonická definice

**EvO je evoluční operátor přípustných stavů nad aktuální realitou.**

Pravidla, fyzikální podmínky, omezení a invarianty určují, co je možné. EvO je nemění. Pracuje nad aktuálně realizovanou realitou `R_t`, společným polem lokálních realit a vazeb `H_t`, realizovanou historií a deklarovaným cílem `G`.

Přípustnost cíle není totožná s tím, že izolovaný cíl splňuje jednotlivá lokální omezení. Kanonický existenční kontrakt je:

\[
\boxed{E_{EvO}(G\mid H_t)=1 \iff \exists\Gamma:\;R_t\rightsquigarrow G}
\]

`∃Γ` **neznamená, že EvO cestu Γ vypočítává**. Je to existenční vlastnost struktury `H_t`: v aktuální realitě musí existovat alespoň jedna koherentní návaznost vedoucí k cíli.

Proto je veřejné rozdělení úloh ostré:

\[
\boxed{EvO:\;\text{JE TO PŘÍPUSTNÉ?}}
\quad\longrightarrow\quad
\boxed{Worker:\;\text{JAK TO REALIZOVAT?}}
\]

Worker nesmí dostat realizační nebo optimalizační úlohu dříve, než platí:

\[
G\in\Omega(H_t).
\]

Pokud je cíl přípustný, teprve Worker smí optimalizovat konkrétní realizaci:

\[
\boxed{\Gamma^*=\arg\min_{\Gamma\in\mathcal P(R_t,G)}J(\Gamma)}
\]

Worker optimalizuje **realizaci**, nikoli mapu reality a nikoli pravidla.

## Dva různé negativní výsledky

`G \notin \Omega(H_t)` má dvě odlišné příčiny.

### 1. Přímý konflikt

Cíl porušuje explicitní omezení:

\[
C_k(G)=0.
\]

Výstupní třída:

`DIRECT_CONFLICT`

### 2. Nedosažitelný stav z aktuální reality

Izolovaný cíl splňuje lokální omezení,

\[
\forall k:\;C_k(G)=1,
\]

ale z aktuální realizované historie neexistuje koherentní návaznost:

\[
\nexists\Gamma:\;R_t\rightsquigarrow G.
\]

Výstupní třída:

`UNREACHABLE_FROM_CURRENT_REALITY`

To je zásadní rozdíl: stav může být sám o sobě legální, ale nemůže vzniknout z této konkrétní historie reality.

## Diagnostika selhání

Negativní výsledek má kontrakt:

\[
\boxed{FAIL(G)=(C_{fail},V_{fail},H_{break})}
\]

kde:

- `C_fail` — omezení, která cíl porušuje,
- `V_fail` — vazby, které konflikt vytvářejí nebo přenášejí,
- `H_break` — místo/kontext, kde přestává existovat koherentní návaznost.

PartnerProf **nesmí neznámé části diagnostiky domýšlet**. Pokud je aktuální CML/CML_A audit neumí autoritativně určit, zůstávají explicitně nevyplněné.

## Nejbližší přípustný cíl

Pokud je původní `G` nepřípustný a uživatel tuto úlohu výslovně požaduje, další samostatný problém je:

\[
\boxed{G^*=\arg\min_{G'\in\Omega(H_t)}d(G',G)}
\]

Ani tato úloha nesmí být nahrazena heuristickým score nebo samovolnou změnou cíle.

## Neměnnost pravidel

\[
\boxed{C_{t+1}=C_t}
\]

Evoluuje operátor nad aktuální realitou, nikoli pravidla.

## Vstupní kontrakt PartnerProfu

1. `CURRENT_REALITY` — aktuální realizovaný stav `R_t`.
2. `LOCAL_REALITIES` — lokální reality/subsystémy společného pole.
3. `RELATIONS` — vazby `V` mezi lokálními realitami/stavy.
4. `CONSTRAINTS` — explicitní omezení `C`.
5. `INVARIANTS` — podmínky, které se při realizaci nesmí porušit.
6. `REALIZED_HISTORY` — realizovaná historie/context `H_t`.
7. `GOAL` — požadovaný cílový stav `G`.
8. `QUESTION` — požadovaná otázka (`ADMISSIBILITY`, `REALIZATION`, `CONFLICT_DIAGNOSTIC`, `NEAREST_ADMISSIBLE_GOAL`, `FULL_CYCLE`).
9. `OPTIMIZATION` — volitelný Worker požadavek `J(Γ)`, který je blokován do kladného výsledku EvO.

`QUESTION` a `OPTIMIZATION` nemění samotné pole reality ani pravidla. Jsou požadavkem na způsob zpracování výsledku a Worker fázi.

## Výstupní kontrakt PartnerProfu

EvO vrací nejprve přípustnost cíle:

- `ADMISSIBLE`, nebo
- `NOT_ADMISSIBLE`.

Při negativním výsledku se rozlišuje, pokud je to autoritativně doloženo:

- `DIRECT_CONFLICT`, nebo
- `UNREACHABLE_FROM_CURRENT_REALITY`.

Diagnostický objekt má tvar `FAIL(G)=(C_fail,V_fail,H_break)`.

Worker gate:

- `OPEN` pouze pokud `E_EvO(G|H_t)=1`,
- `CLOSED` pokud `E_EvO(G|H_t)=0`.

Samotný EvO výstup **není cesta Γ** a nesmí být prezentován jako optimalizovaná realizace.

## Šachová manifestace

Šachy jsou diskrétní manifestace stejného kontraktu. Pravidla hry jsou neměnná `C`, aktuální pozice je `R_t`, historie tahů je realizovaná historie a `G = CHECKMATE(opponent)`.

Tah může být podle pravidel legální a přesto nepřípustný, pokud po něm neexistuje koherentní návaznost k cíli. EvO pravidla šachu nemění. Worker/šachový realizační mechanismus smí volit konkrétní cestu pouze v krajině, kterou EvO předtím připustil.

### Počáteční směrový vektor šachové manifestace

Výchozí šachová pozice sama neurčuje nenulový směr evoluce. Proto je jediným ručním zásahem první legální tah bílých:

\[
\Delta R_0 = R_1-R_0 = v_0,\qquad v_0\neq 0.
\]

Tento tah není publikací EvO ani výsledkem Workeru. Je to externě realizovaný počáteční směrový vektor, který se předá EvO/CML jako první člen realizované historie. V tomto seed kroku se nepožaduje kompenzační tah EvO.

Následuje reakce soupeře:

\[
R_1 \xrightarrow{\mathrm{Stockfish}} R_2.
\]

Teprve z této změněné aktuální reality pokračuje EvO:

\[
\mathrm{EvO}_t(R_t,H_t,C,G)\rightarrow\mathcal A_t,\qquad t\ge 2.
\]

Od tohoto okamžiku uživatel tahy neřídí. EvO hraje stranu, jejíž počáteční směr byl ručně zaveden, Stockfish je soupeř a po každé jeho reakci EvO evoluuje další přípustný stav z realizované historie a právě aktuální reality. Pravidla `C` se tím nemění.

## Application neutrality of EvO/CML

EvO is not specialized for chess. The same CML/CML_A machinery is used by different applications. An application is responsible only for representing its current reality as a numeric field and for projecting the returned numeric realization back into that application's state space.

For the chess manifestation this means that the current reality first generates only its rule-legal immediate local realities:

\[
\mathcal K_t=\{R_t^{(1)},R_t^{(2)},\ldots,R_t^{(n)}\}.
\]

The field contains the realized state, the realized history/change, invariant rules and goal, the candidate-local-reality transition vectors, and the condensed consequence of the previous CML result:

\[
F_{t,k}=H(R_t,\widetilde H_t,\Delta R_t,C,G,\mathcal K_{t,k},V_{t,k}).
\]

Only one numeric vector crosses the public boundary:

\[
Y_{t,k}=\mathrm{CML}(F_{t,k}).
\]

The application then reads `Y_{t,k}` only in relation to the candidate blocks of the same `F_{t,k}`. If one candidate remains the returned most-relevant realization it is manifested. If no candidate realization exists the result is `NO_REALIZATION`. If several candidate states remain equally returned, determinism has not yet arisen and reality does not change:

\[
|\mathcal A_{t,k}|>1\quad\Rightarrow\quad F_{t,k+1}=\operatorname{Recombine}(F_{t,k},Y_{t,k})\rightarrow\mathrm{CML}.
\]

Thus `MULTIPLE_ADMISSIBLE_STATES` means further evolution over the same current reality, never an external tie-break and never a false terminal result. The application does not evaluate chess positions and does not prescribe prediction or Hessenberg evolution.

Only after a single state is returned does determinism appear as the realized result:

\[
Y_{t,k}\rightarrow R_{t+1}.
\]

The realized `R_{t+1}` is immediately written back into the field and the CML result is condensed into `\widetilde H_{t+1}` before waiting for the opponent. The full sequence remains separately visible in the audit trail. After the external opponent changes reality,

\[
R_{t+1}\xrightarrow{\text{opponent}}R_{t+2},
\]

its realized delta and the new candidate local realities are integrated with the condensed evolved history and the same public CML gateway is invoked again. Rules remain invariant; the operator evolves over the newly realized current reality.
