Import-Module PSOpenAI

$r = Request-ChatCompletion -Message "summarise the open tickets for this agent"
Write-Output $r.Answer
