// Synthetic, non-working sample for the CodeDelta Agent Scan demo. Never executed.
using System;
using System.Diagnostics;
using System.Threading.Tasks;
using Microsoft.SemanticKernel;

namespace Demo.Agents
{
    public class KernelPlanner
    {
        private readonly Kernel kernel;

        public KernelPlanner()
        {
            kernel = new Kernel();
            kernel.add_plugin(new ShellPlugin(), "shell");
        }

        public async Task<string> PlanAsync(string goal)
        {
            var result = await kernel.InvokeAsync("planner", "plan", new() { ["goal"] = goal });
            return result.ToString();
        }

        // Agent output handed straight to the operating system.
        public async Task ExecutePlanAsync(string goal)
        {
            var plan = await PlanAsync(goal);
            Process.Start("/bin/sh", "-c " + plan);
        }
    }

    public class ShellPlugin
    {
        public string Run(string command) => command;
    }
}
