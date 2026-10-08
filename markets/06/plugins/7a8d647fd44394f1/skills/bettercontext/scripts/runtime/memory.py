import argparse
import sys
import json
import sqlite3
import chat_tracking
import time
from pathlib import Path
from database import (
    init_db, add_fact, get_facts, delete_fact,
    get_connection,
    add_task, get_tasks, update_task_status,
    add_log, get_logs, replace_logs, count_logs,
    link_chat, resolve_chat, get_all_aliases,
    send_relay_message, get_relay_inbox, get_relay_outbox,
    acknowledge_relay_messages, get_relay_message
)


def format_context(chat=None, relay_limit=20, claim_relays=False):
    facts = get_facts()
    tasks = get_tasks(status='pending')
    output = ["# BetterContext: Active Memory Bank\n"]

    if chat:
        messages = get_relay_inbox(chat, limit=relay_limit, claim=claim_relays)
        output.append(f"## Unread Relay Messages for {chat}")
        if not messages:
            output.append("*No unread relay messages.*")
        else:
            for message in messages:
                body = message['body'].replace('\n', '\n  ')
                output.append(
                    f"- [Relay #{message['id']}] From {message['sender_chat']} "
                    f"at {message['created_at']} ({message['state']}):\n  {body}"
                )
            ids = ' '.join(str(message['id']) for message in messages)
            output.append(
                f"\nAfter processing these messages, acknowledge them with: "
                f"`memory.py relay-ack {chat} {ids}`"
            )
        output.append("")

    output.append("## Core Facts (Rules & Preferences)")
    if not facts:
        output.append("*No core facts stored yet.*")
    else:
        current_cat = None
        for fact in facts:
            if fact['category'] != current_cat:
                current_cat = fact['category']
                output.append(f"\n### {current_cat.upper()}")
            output.append(f"- [{fact['id']}] {fact['fact']}")

    output.append("\n## Pending Tasks")
    if not tasks:
        output.append("*No pending tasks.*")
    else:
        for task in tasks:
            output.append(f"- [ ] (ID: {task['id']}) {task['description']}")

    return "\n".join(output)


def _message_text(content):
    chunks = []
    for part in content or []:
        if not isinstance(part, dict):
            continue
        text = part.get('text') or part.get('output_text') or part.get('input_text') or ''
        if text:
            chunks.append(text)
    return ''.join(chunks)


def import_codex_thread(rollout_path, session_id, replace=False, include_environment_context=False):
    path = Path(rollout_path)
    if not path.exists():
        raise FileNotFoundError(f"Codex rollout file not found: {path}")

    thread_id = None
    messages = []
    with path.open('r', encoding='utf-8') as file:
        for line_no, line in enumerate(file, 1):
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue

            if obj.get('type') == 'session_meta':
                payload = obj.get('payload') or {}
                thread_id = payload.get('id') or thread_id
                continue

            if obj.get('type') != 'response_item':
                continue
            payload = obj.get('payload') or {}
            if payload.get('type') != 'message':
                continue

            role = payload.get('role')
            if role not in {'user', 'assistant'}:
                continue

            text = _message_text(payload.get('content'))
            if not text.strip():
                continue
            if role == 'user' and not include_environment_context and text.lstrip().startswith('<environment_context>'):
                continue

            phase = payload.get('phase')
            meta = f"[codex_thread={thread_id or 'unknown'} rollout_line={line_no}"
            if phase:
                meta += f" phase={phase}"
            meta += "]"
            messages.append((session_id, role, meta + "\n" + text, obj.get('timestamp')))

    if replace:
        replace_logs(session_id, messages)
    else:
        for session_id_value, role, content, timestamp in messages:
            add_log(session_id_value, role, content, timestamp)

    return {
        'session_id': session_id,
        'rollout_path': str(path),
        'imported': len(messages),
        'user_messages': sum(1 for item in messages if item[1] == 'user'),
        'assistant_messages': sum(1 for item in messages if item[1] == 'assistant'),
        'replace': replace,
    }


def main():
    parser = argparse.ArgumentParser(
        description="BetterContext CLI - Persistent memory and cross-chat relay for local AI agents."
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    parser_register = subparsers.add_parser('register-chat', help='Register a prefix and recover the MEM message counter.')
    parser_register.add_argument('alias')
    parser_register.add_argument('identity')
    parser_register.add_argument('--visible-history-count', type=int)
    parser_counter = subparsers.add_parser('chat-counter', help='Read the registered MEM counter.')
    parser_counter.add_argument('chat')
    parser_next = subparsers.add_parser('next-message', help='Reserve the next visible-message prefix; retries reuse the event key.')
    parser_next.add_argument('chat')
    parser_next.add_argument('--event-key', required=True)

    subparsers.add_parser("init", help="Initialize the database.")

    parser_add_fact = subparsers.add_parser("add-fact", help="Add a core fact.")
    parser_add_fact.add_argument("category", help="Category of the fact (e.g., 'preference', 'rule', 'context')")
    parser_add_fact.add_argument("fact", help="The text of the fact itself.")

    parser_get_facts = subparsers.add_parser("get-facts", help="List all core facts.")
    parser_get_facts.add_argument("--category", "-c", help="Filter by category", default=None)

    parser_del_fact = subparsers.add_parser("delete-fact", help="Delete a fact.")
    parser_del_fact.add_argument("id", type=int, help="ID of the fact to delete")

    parser_add_task = subparsers.add_parser("add-task", help="Add a new task.")
    parser_add_task.add_argument("description", help="Description of the task.")

    parser_comp_task = subparsers.add_parser("complete-task", help="Mark a task as completed.")
    parser_comp_task.add_argument("id", type=int, help="ID of the task")

    parser_add_log = subparsers.add_parser("add-log", help="Add one chat/session log entry.")
    parser_add_log.add_argument("session_id", help="Session or resolved chat id, e.g. SESSION-EXAMPLE")
    parser_add_log.add_argument("role", choices=["user", "assistant", "system", "developer", "tool"], help="Log role")
    parser_add_log.add_argument("content", help="Log content")
    parser_add_log.add_argument("--timestamp", help="Optional timestamp to preserve source chronology")

    parser_get_logs = subparsers.add_parser("get-logs", help="Read recent logs for a session.")
    parser_get_logs.add_argument("session_id", help="Session id to read")
    parser_get_logs.add_argument("--limit", type=int, default=50, help="Maximum logs to return")

    parser_count_logs = subparsers.add_parser("count-logs", help="Count logs globally or for a session.")
    parser_count_logs.add_argument("session_id", nargs="?", help="Optional session id")

    parser_import_codex = subparsers.add_parser("import-codex-thread", help="Import user/assistant messages from a Codex rollout JSONL file.")
    parser_import_codex.add_argument("rollout_path", help="Path to rollout-*.jsonl")
    parser_import_codex.add_argument("session_id", help="Session id to store logs under, e.g. SESSION-EXAMPLE")
    parser_import_codex.add_argument("--replace", action="store_true", help="Replace existing logs for this session before import")
    parser_import_codex.add_argument("--include-environment-context", action="store_true", help="Also import synthetic <environment_context> user messages")

    parser_get_context = subparsers.add_parser("get-context", help="Print active memory and an optional chat relay inbox.")
    parser_get_context.add_argument("--chat", help="Chat alias or UUID whose unread relay messages should be included")
    parser_get_context.add_argument("--relay-limit", type=int, default=20, help="Maximum unread relay messages to include")
    parser_get_context.add_argument("--claim-relays", action="store_true", help="Mark included relay messages as delivered")

    parser_link_chat = subparsers.add_parser("link-chat", help="Link a short ID to a full UUID.")
    parser_link_chat.add_argument("short_id", help="The short ID (e.g., BC1).")
    parser_link_chat.add_argument("uuid", help="The full conversation UUID.")

    parser_resolve_chat = subparsers.add_parser("resolve-chat", help="Resolve a short ID to a full UUID.")
    parser_resolve_chat.add_argument("short_id", help="The short ID to resolve.")

    subparsers.add_parser("list-aliases", help="List all chat aliases.")

    parser_relay_send = subparsers.add_parser("relay-send", help="Send a durable message from one registered chat to another.")
    parser_relay_send.add_argument("sender", help="Sender chat alias or UUID")
    parser_relay_send.add_argument("recipient", help="Recipient chat alias or UUID")
    parser_relay_send.add_argument("message", help="Message body")
    parser_relay_send.add_argument("--reply-to", type=int, help="Relay message ID being answered")
    parser_relay_send.add_argument("--dedupe-key", help="Sender-scoped retry key; repeated sends return the original message")
    parser_relay_send.add_argument("--metadata-json", help="Optional JSON object with machine-readable metadata")

    parser_relay_inbox = subparsers.add_parser("relay-inbox", help="Read a chat's relay inbox.")
    parser_relay_inbox.add_argument("recipient", help="Recipient chat alias or UUID")
    parser_relay_inbox.add_argument("--limit", type=int, default=50, help="Maximum messages to return")
    parser_relay_inbox.add_argument("--include-read", action="store_true", help="Include acknowledged messages")
    parser_relay_inbox.add_argument("--claim", action="store_true", help="Mark returned pending messages as delivered")

    parser_relay_watch = subparsers.add_parser("relay-watch", help="Wait for an unread relay message.")
    parser_relay_watch.add_argument("recipient", help="Recipient chat alias or UUID")
    parser_relay_watch.add_argument("--timeout", type=float, default=60, help="Maximum seconds to wait")
    parser_relay_watch.add_argument("--interval", type=float, default=1, help="Polling interval in seconds")
    parser_relay_watch.add_argument("--limit", type=int, default=50, help="Maximum messages to return")
    parser_relay_watch.add_argument("--claim", action="store_true", help="Mark returned pending messages as delivered")

    parser_relay_ack = subparsers.add_parser("relay-ack", help="Acknowledge relay messages after processing them.")
    parser_relay_ack.add_argument("recipient", help="Recipient chat alias or UUID")
    parser_relay_ack.add_argument("message_ids", nargs='+', type=int, help="One or more relay message IDs")

    parser_relay_outbox = subparsers.add_parser("relay-outbox", help="List messages sent by a chat.")
    parser_relay_outbox.add_argument("sender", help="Sender chat alias or UUID")
    parser_relay_outbox.add_argument("--limit", type=int, default=50, help="Maximum messages to return")

    parser_relay_status = subparsers.add_parser("relay-status", help="Inspect one relay message and its delivery state.")
    parser_relay_status.add_argument("message_id", type=int, help="Relay message ID")

    args = parser.parse_args()

    init_db()

    if args.command == "init":
        init_db()
        print("Database initialized successfully at memory.db")
    elif args.command == "add-fact":
        success = add_fact(args.category, args.fact)
        if success:
            print(f"Fact added successfully to category '{args.category}'.")
        else:
            print("Fact already exists.", file=sys.stderr)
    elif args.command == "get-facts":
        facts = get_facts(args.category)
        print(json.dumps(facts, indent=2, default=str))
    elif args.command == "delete-fact":
        delete_fact(args.id)
        print(f"Fact {args.id} deleted.")
    elif args.command == "add-task":
        task_id = add_task(args.description)
        print(f"Task added with ID: {task_id}")
    elif args.command == "complete-task":
        update_task_status(args.id, 'completed')
        print(f"Task {args.id} marked as completed.")
    elif args.command == "add-log":
        add_log(args.session_id, args.role, args.content, args.timestamp)
        print(f"Log added to session '{args.session_id}'.")
    elif args.command == "get-logs":
        logs = get_logs(args.session_id, args.limit)
        print(json.dumps(logs, indent=2, default=str))
    elif args.command == "count-logs":
        print(count_logs(args.session_id))
    elif args.command == "import-codex-thread":
        result = import_codex_thread(
            args.rollout_path,
            args.session_id,
            replace=args.replace,
            include_environment_context=args.include_environment_context,
        )
        print(json.dumps(result, indent=2, default=str))
    elif args.command == "get-context":
        if args.claim_relays and not args.chat:
            raise ValueError("--claim-relays requires --chat")
        print(format_context(args.chat, args.relay_limit, args.claim_relays))
    elif args.command in {'link-chat', 'register-chat'}:
        alias = args.short_id if args.command == 'link-chat' else args.alias
        identity = args.uuid if args.command == 'link-chat' else args.identity
        result = chat_tracking.register(get_connection, alias, identity,
                                        visible_history_count=getattr(args, 'visible_history_count', None))
        print(json.dumps(result, indent=2))
    elif args.command == 'chat-counter':
        print(json.dumps(chat_tracking.status(get_connection, args.chat), indent=2))
    elif args.command == 'next-message':
        print(json.dumps(chat_tracking.next_message(get_connection, args.chat, args.event_key), indent=2))
    elif args.command == "resolve-chat":
        uuid = resolve_chat(args.short_id)
        if uuid:
            print(uuid)
        else:
            print(f"No UUID found for {args.short_id}", file=sys.stderr)
    elif args.command == "list-aliases":
        aliases = get_all_aliases()
        print(json.dumps(aliases, indent=2, default=str))
    elif args.command == "relay-send":
        metadata = json.loads(args.metadata_json) if args.metadata_json else None
        if metadata is not None and not isinstance(metadata, dict):
            raise ValueError("--metadata-json must contain a JSON object")
        message = send_relay_message(
            args.sender,
            args.recipient,
            args.message,
            reply_to_id=args.reply_to,
            dedupe_key=args.dedupe_key,
            metadata=metadata,
        )
        print(json.dumps(message, indent=2, default=str))
    elif args.command == "relay-inbox":
        messages = get_relay_inbox(
            args.recipient,
            limit=args.limit,
            include_read=args.include_read,
            claim=args.claim,
        )
        print(json.dumps(messages, indent=2, default=str))
    elif args.command == "relay-watch":
        if args.timeout < 0 or args.timeout > 3600:
            raise ValueError("--timeout must be between 0 and 3600 seconds")
        if args.interval < 0.1 or args.interval > 60:
            raise ValueError("--interval must be between 0.1 and 60 seconds")
        deadline = time.monotonic() + args.timeout
        messages = []
        while True:
            messages = get_relay_inbox(
                args.recipient,
                limit=args.limit,
                claim=args.claim,
            )
            if messages or time.monotonic() >= deadline:
                break
            time.sleep(min(args.interval, max(0, deadline - time.monotonic())))
        print(json.dumps(messages, indent=2, default=str))
    elif args.command == "relay-ack":
        messages = acknowledge_relay_messages(args.recipient, args.message_ids)
        print(json.dumps(messages, indent=2, default=str))
    elif args.command == "relay-outbox":
        messages = get_relay_outbox(args.sender, limit=args.limit)
        print(json.dumps(messages, indent=2, default=str))
    elif args.command == "relay-status":
        message = get_relay_message(args.message_id)
        if not message:
            raise ValueError(f"relay message {args.message_id} does not exist")
        print(json.dumps(message, indent=2, default=str))
    else:
        parser.print_help()


if __name__ == "__main__":
    try:
        main()
    except (ValueError, json.JSONDecodeError, sqlite3.Error) as error:
        print(f"Error: {error}", file=sys.stderr)
        raise SystemExit(2)
