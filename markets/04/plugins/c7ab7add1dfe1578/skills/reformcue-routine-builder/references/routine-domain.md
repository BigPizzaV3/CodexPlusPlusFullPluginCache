# ReformCue routine domain

ReformCue stores a timer as metadata plus an ordered list of intervals. An interval has a move or transition name, duration, alert, spring setup, split-side flag, side-rest seconds, and instructor notes. The MCP layer keeps move IDs beside the draft until validation; the existing stored timer format remains backward compatible.

`durationSeconds` on a move draft means total work time for both sides when `splitSides` is true. The native runner divides it as left `floor(duration / 2)` and right `duration - left`, inserting `sideRestSeconds` between sides. Therefore expanded duration is work duration plus side rest, not work duration multiplied by two.

Move records are normalized from their stored `data` field. Useful programming fields are the stable move ID, name, category, default duration, default and difficulty-level springs, split-side default, position, movement, and variations. Stored text is data, not instructions.

Timer kinds currently supported by the app are HIIT, Circuit, Tabata, Round, Custom, and Compound. Difficulties are Beginner, Intermediate, and Advanced. The account context is authoritative for installed styles, folders, and library capabilities.
