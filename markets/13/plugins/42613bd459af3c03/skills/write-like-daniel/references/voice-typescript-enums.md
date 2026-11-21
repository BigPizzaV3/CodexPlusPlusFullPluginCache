# Style reference: Nine terrible ways to use TypeScript enums, and one good way.

Source: https://bluepnume.medium.com/nine-terrible-ways-to-use-typescript-enums-and-one-good-way-f9c7ec68bf15 (2024). Opening excerpt, for voice and rhythm only; use search for the argument.

TypeScript enums get a lot of hate. And not for an unjustified reason: they have so many potential foot-guns.
But — my position is, they still belong in the language rather than out. Like the proverbial doctor advising the patient whose arm hurts when he moves it like that, I’ll argue: just don’t move it like that.
I do believe that a future major version of TypeScript should remove or obviate a lot of these anti-patterns, though.

### 1. Don’t rely on implicit values

One way to write an enum in Typescript is:

```
enum Suit {
Hearts,
Diamonds,
Clubs,
Spades
}
```

This transpiles to something similar to:

```
const Suit = {
Hearts: 0,
Diamonds: 1,
Clubs: 2,
Spades: 3
}
```

Obviously, this is awful. Re-order the enum keys, or add new enum keys, and you risk changing the automatically generated enum values.

### 2. Don’t define explicit numeric values

When you do, you end up with a weird result:

```
enum Suit {
Hearts = 0,
Diamonds = 1,
Clubs = 2,
Spades = 3
}
```

Transpiles to:

```
const Suit = {
Hearts: 0,
Diamonds: 1,
Clubs: 2,
Spades: 3,
0: 'Hearts',
1: 'Diamonds',
2: 'Clubs',
3: 'Spades'
}
```

For whatever reason, this does not happen if you use string enum values.
I believe this is done to allow you to do a reverse lookup of the key, more easily, for example:

```
const heartsKey = Suit[Suit.Hearts];
```

But this brings us to the next tip:

### 3. Don’t do reverse lookups of enum keys

There isn’t really a good reason to do things like this.

```
const heartsKey = Suit[Suit.Hearts];
```

The values of an enum should be significant to your code. The key names are an implementation detail, and only really serve to make your code more readable.
If you need a descriptive name, just define a new mapping of enum value to name.

### 4. Don’t use numeric enum values in functions

Yeah, these things really suck.

```
enum Suit {
Hearts = 0,
Diamonds = 1,
Clubs = 2,
Spades = 3
}

function logSuit(suit : Suit) {
console.log(suit);
}

logSuit(1337);
```

This doesn’t raise a type error. So really what’s the point of even having the enum at this point?

### 5. Don’t use literal values when the type is enum

One of the common arguments against enums is: “I can’t pass a literal value, even if it belongs to the enum”

```
enum Suit {
Hearts = 'hearts',
Diamonds = 'diamonds',
Clubs = 'clubs',
Spades = 'spades'
}

function logSuit(suit : Suit) {
console.log(suit);
}

logSuit('hearts');

// Argument of type '"hearts"' is not assignable to parameter of type 'Suit'.(2345)
```
