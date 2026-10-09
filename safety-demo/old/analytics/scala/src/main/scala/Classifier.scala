import io.cequence.openaiscala.service.OpenAIServiceFactory

object Classifier {
  val service = OpenAIServiceFactory()
  def label(body: String) = {
    val reply = service.createChatCompletion(messages)
    println(reply)
  }
}
