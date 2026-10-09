require "openai"

client = OpenAI::Client.new
r = client.chat(parameters: { model: "gpt-4o", messages: msgs })
puts r.dig("choices", 0, "message", "content")
