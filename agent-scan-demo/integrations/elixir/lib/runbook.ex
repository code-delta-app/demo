defmodule Meridian.Runbook do
  alias LangChain.ChatModels.ChatOpenAI
  alias LangChain.Chains.LLMChain

  def apply_fix(incident) do
    {:ok, chain} = %{llm: ChatOpenAI.new!(%{model: "gpt-4o"})} |> LLMChain.new!() |> LLMChain.run()
    System.cmd("sh", ["-c", chain.last_message.content])
  end
end
