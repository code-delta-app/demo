defmodule Meridian.Summarizer do
  alias LangChain.ChatModels.ChatOpenAI
  alias LangChain.Chains.LLMChain

  def summarise(messages) do
    {:ok, chain} = %{llm: ChatOpenAI.new!(%{model: "gpt-4o"})} |> LLMChain.new!() |> LLMChain.run()
    IO.puts(chain.last_message.content)
  end
end
