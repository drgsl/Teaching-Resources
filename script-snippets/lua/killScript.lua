













script.Parent.Touched:connect(
    function(hit)
        if hit.Parent:FindFirstChild("Humanoid") then
            hit.Parent.Humanoid.Health = 0
    end
end)








