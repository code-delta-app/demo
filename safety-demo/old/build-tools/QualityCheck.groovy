import com.openai.client.OpenAIClient

class QualityCheck {
  OpenAIClient client

  String review(String diff) {
    def reply = client.chat().completions().create(params)
    println reply
    return reply
  }
}
