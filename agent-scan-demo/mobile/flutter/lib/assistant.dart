import 'package:dart_openai/dart_openai.dart';

Future<String> draftReply(String ticket) async {
  final chat = await OpenAI.instance.chat.create(model: 'gpt-4o', messages: []);
  return chat.choices.first.message.content.toString();
}
