// JavaScript/TypeScript AI usage — Agent Scan covers JS SDKs too.
import OpenAI from "openai";
import Anthropic from "@anthropic-ai/sdk";

const openai = new OpenAI();
const anthropic = new Anthropic();

export async function ask(question) {
  const r = await openai.chat.completions.create({
    model: "gpt-4o",
    messages: [{ role: "user", content: question }],
  });
  return r.choices[0].message.content;
}

export async function summarise(text) {
  return anthropic.messages.create({
    model: "claude-opus-4-8",
    max_tokens: 256,
    messages: [{ role: "user", content: `Summarise: ${text}` }],
  });
}
