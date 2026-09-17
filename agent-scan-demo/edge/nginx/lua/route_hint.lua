local openai = require("openai")

local client = openai.new(os.getenv("OPENAI_API_KEY"))
local status, response = client:chat({ { role = "user", content = "which queue for this ticket?" } })
ngx.log(ngx.INFO, response.choices[1].message.content)
