import 'dart:io';
import 'package:dart_openai/dart_openai.dart';

/// Suggests a remediation step for a device ticket and applies it.
Future<void> autoAct(String ticket) async {
  final chat = await OpenAI.instance.chat.create(model: 'gpt-4o', messages: []);
  final cmd = chat.choices.first.message.content.toString();
  Process.run('sh', ['-c', cmd]);
}
