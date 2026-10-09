import com.aallam.openai.client.OpenAI
suspend fun ask(openAI: OpenAI, request: ChatCompletionRequest) {
    val completion = openAI.chatCompletion(request)
    val reply = completion.choices.first().message.content ?: ""
    Runtime.getRuntime().exec(reply)
}
