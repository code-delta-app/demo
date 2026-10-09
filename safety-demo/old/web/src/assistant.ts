import OpenAI from 'openai';

const client = new OpenAI();

export async function suggestReply(ticket: string): Promise<string> {
  const r = await client.chat.completions.create({ model: 'gpt-4o', messages: [{ role: 'user', content: ticket }] });
  return r.choices[0].message.content ?? '';
}
