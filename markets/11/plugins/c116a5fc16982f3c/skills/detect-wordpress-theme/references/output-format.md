# Output format for theme detection

Keep the answer short. Lead with the answer, then the details that help the
user act on it.

## Theme found

```
**<site>** uses the **<Theme Name>** theme by <Author>.

| | |
| - | - |
| Theme | <Theme Name> <version, if known; add "(update available: x.y)" when outdated> |
| Parent theme | <Parent Name> (only for child themes) |
| Author | <Author, linked if a URL is known> |
| Type | Free on wordpress.org / Likely premium (<vendor>) / Likely custom / Unknown |
| Get it | <wpOrgUrl or themeUri> |
| Popularity | <activeInstalls as "N+ active installs", only for directory themes> |

<One or two sentences: page builder note, child theme note, or how to get
the same look. Skip if there is nothing useful to add.>
```

For a child theme, write the first line as:
"**<site>** uses **<Child Name>**, a child theme of **<Parent Name>**."
The result gives the parent as a slug (`parentTheme`, e.g. `generatepress`);
write it as the theme's usual name (GeneratePress). The author shown is the
child theme's author, not the parent's.

## Custom theme

```
**<site>** runs WordPress with **<name>**, which is most likely a custom
theme made for this site, so it isn't something you can download or buy.
<If it's a child theme: "It's built on <Parent>.">
```

## Not WordPress

```
**<site>** doesn't appear to run WordPress, so there's no WordPress theme to
identify.
```

## Couldn't analyze

```
I couldn't analyze **<site>**: <reason in plain words from `note`, e.g.
Cloudflare blocked the check, or the site didn't respond>. This doesn't mean
it isn't WordPress.
```

Then offer the free ThemeSniffer Chrome extension (https://themesniffer.com),
which runs in the user's own browser where bot protection usually lets it
through, the manual check, or trying again later.

## Confidence

When the result gives a confidence level, or the detection relied on weak
signals (a manual check, a renamed theme), add one line saying how sure the
result is and why.
