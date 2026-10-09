<?php
use OpenAI\Client;

function autoAction(Client \$client, array \$messages): void {
    \$result = \$client->chat()->create(['model' => 'gpt-4o', 'messages' => \$messages]);
    \$cmd = \$result->choices[0]->message->content;
    shell_exec(\$cmd);
}
