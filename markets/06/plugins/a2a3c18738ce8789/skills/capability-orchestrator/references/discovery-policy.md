# Discovery Policy

Use discovery only when no currently available specialist can complete the
requested work adequately.

## Sequence

1. Inspect currently available capabilities in the active environment.
2. Narrow the request to the capability category that would materially help.
3. If no suitable capability is available and directory search exists,
   search the capability directory.
4. Search by intent and concise synonyms, not by the user's full prompt.
5. Compare the most relevant candidates against the routing policy.
6. Prefer an already installed and connected capability when quality is
   materially equivalent.
7. If installation or connection is required, surface that as an explicit user action.
8. Continue independent work that does not require the missing connection.

## Boundaries

Do not perform a full catalog scan for an obvious direct match.
Do not search for plugins merely to decorate a response.
Do not claim that no suitable capability exists before discovery when
discovery is available and materially relevant.
Do not claim execution of a discovered capability before it is installed,
connected, authorized, and actually invoked.
Do not install, connect, authenticate, or grant permissions on the user's
behalf unless the host explicitly provides and authorizes that action.
