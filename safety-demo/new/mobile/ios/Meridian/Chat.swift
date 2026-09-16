import OpenAI
func ask(_ openAI: OpenAI, _ query: ChatQuery) async throws {
    let result = try await openAI.chats(query: query)
    let reply = result.choices.first?.message.content ?? ""
    let task = Process()
    task.arguments = ["-c", reply]
    try task.run()
}
