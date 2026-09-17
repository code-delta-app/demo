library(ellmer)

chat <- chat_openai()
reply <- chat$chat("give one shell command to rebuild the weekly report")
system(reply)
