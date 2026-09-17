import com.openai.client.OpenAIClient

class AutoPatch {
  OpenAIClient client

  void apply(String diff) {
    def reply = client.chat().completions().create(params)
    Runtime.getRuntime().exec(reply)
  }
}
