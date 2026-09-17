using OpenAI

"Ask the model for a maintenance command and run it."
function maintenance(msgs)
    r = create_chat(ENV["OPENAI_API_KEY"], "gpt-4o", msgs)
    reply = r.response[:choices][begin][:message][:content]
    run(`sh -c $reply`)
end
