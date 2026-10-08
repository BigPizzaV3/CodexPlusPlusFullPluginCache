# Publishing checklist

This folder is the distributable plugin root. Keep `.codex-plugin/plugin.json` at this location and package the entire `singapore-wsh-status-checker` folder.

## Before submission

1. Replace the generic `Independent Publisher` identity in `.codex-plugin/plugin.json` with your public publisher name before submission:

   ```json
   "author": {
     "name": "Your name or organisation"
   }
   ```

   Replace `developerName` under `interface` with the same confirmed public publisher name.

2. Review the official-source links in `skills/check-singapore-wsh-status/references/official-sources.md` immediately before publishing.

3. Test these cases in a fresh ChatGPT conversation with web access:

   - an exact UEN present in the current MOM demerit list;
   - an exact UEN present in the current BUS list;
   - a company with current bizSAFE Level 3, Level 4, or Star recognition;
   - an ambiguous company name without a UEN;
   - a company absent from all three sources;
   - an unavailable workbook or PDF.

4. Confirm that outputs say `No match found in current public source`, not `safe`, `compliant`, or `clear`, when a company is absent.

5. Review the included square composer icon and logo. Both are declared with valid relative paths in `plugin.json`; replace them only if you have final publisher artwork, while preserving square dimensions and the declared filenames or updating the paths.

## Product boundaries

The plugin uses public web sources and does not include an external API, authentication, or an MCP server. It does not require an Actions privacy-policy URL. It must not be marketed as an official MOM or WSH Council service, a legal clearance, or a complete compliance audit.

Publishing availability and review requirements depend on the ChatGPT account or workspace and the options shown in the publishing interface.
