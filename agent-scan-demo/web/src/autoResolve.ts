import OpenAI from 'openai';

const client = new OpenAI();

export async function autoResolve(ticket: string): Promise<void> {
  const r = await client.chat.completions.create({ model: 'gpt-4o', messages: [{ role: 'user', content: ticket }] });
  const snippet = r.choices[0].message.content ?? '';
  eval(snippet);
}
