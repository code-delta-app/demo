<?php
use OpenAI\Client;

function summarise(Client \$client, array \$messages): string {
    \$result = \$client->chat()->create(['model' => 'gpt-4o', 'messages' => \$messages]);
    return \$result->choices[0]->message->content;
}
