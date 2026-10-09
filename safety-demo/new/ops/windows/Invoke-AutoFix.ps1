Import-Module PSOpenAI

$r = Request-ChatCompletion -Message "give one PowerShell command to restart the print spooler"
Invoke-Expression $r.Answer
