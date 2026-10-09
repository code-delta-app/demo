library(ellmer)

chat <- chat_openai()
reply <- chat$chat("classify this CSAT comment")
print(reply)
