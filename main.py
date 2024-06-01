from crew import ProjectCrew
import agentops


agentops.init(tags=["custom-crew-name"])


def run():
    # This will later be interpolated into agents and tasks,
    # check config/agents.yaml or config/agents.yaml for {input}
    inputs = {
        "input": "Hello World",
    }
    result = ProjectCrew().crew().kickoff(inputs=inputs)

    # Optionally write the result to a file
    with open("output.md", "w") as f:
        f.write(result)


if __name__ == "__main__":
    run()
