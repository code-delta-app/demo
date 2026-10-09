using PromptingTools

"Score the sentiment of a batch of ticket bodies."
function score(bodies)
    msg = aigenerate("rate the sentiment of this ticket")
    println(msg)
end
