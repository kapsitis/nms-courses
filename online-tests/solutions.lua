-- solutions.lua

local function has_class(el, class)
  if not el.classes then return false end
  for _, c in ipairs(el.classes) do
    if c == class then
      return true
    end
  end
  return false
end

function Pandoc(doc)
  -- read metadata
  local show = false
  local v = doc.meta["show-solutions"]

  if v ~= nil then
    if type(v) == "boolean" then
      show = v
    elseif type(v) == "string" then
      show = (v:lower() == "true")
    end
  end

  io.stderr:write("DEBUG: show-solutions = " .. tostring(show) .. "\n")

  -- define how to treat solution divs
  local function handle_div(div)
    if has_class(div, "solution") then
      io.stderr:write("DEBUG: saw a solution div\n")
      return show and div or {}
    end
    -- leave other Divs unchanged
  end

  -- walk the whole document with that handler
  return doc:walk{ Div = handle_div }
end