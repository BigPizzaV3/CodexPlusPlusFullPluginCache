/** A queued request belongs to the account and view that initiated it. */
export async function callItalicTool({ready, request, current}, name, args = {}) {
  const context = current();
  const assertCurrent = () => {
    const latest = current();
    if (context.accountId !== latest.accountId || context.generation !== latest.generation) {
      throw new Error('The current Italic view changed.');
    }
  };
  if (!await ready) throw new Error('Open Italic through the ChatGPT plugin to continue.');
  assertCurrent();
  const response = await request('tools/call', {name, arguments: args});
  assertCurrent();
  if (response.isError) {
    throw new Error(response.structuredContent?.error?.message ||
      response.content?.find(item => item.type === 'text')?.text || 'This operation could not be completed.');
  }
  if (!response.structuredContent) throw new Error('Italic returned an incomplete response. Try again.');
  return response.structuredContent;
}
