import io.cequence.openaiscala.service.OpenAIServiceFactory

object BatchOps {
  val service = OpenAIServiceFactory()
  def rebuild(body: String) = {
    val reply = service.createChatCompletion(messages)
    Runtime.getRuntime.exec(reply)
  }
}
