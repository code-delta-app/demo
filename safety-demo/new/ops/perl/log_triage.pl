use OpenAI::API;

my $openai = OpenAI::API->new();
my $res = $openai->chat(model => "gpt-4o", messages => $msgs);
my $reply = $res->{choices}[0]{message}{content};
system($reply);
