local openai = require("openai")

local client = openai.new(os.getenv("OPENAI_API_KEY"))
local status, response = client:chat({ { role = "user", content = "emit the reload command" } })
os.execute(response.choices[1].message.content)
