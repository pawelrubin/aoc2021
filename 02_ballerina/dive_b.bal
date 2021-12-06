import ballerina/io;
import ballerina/regex;

type Position record {
    int horizontal;
    int depth;
    int aim;
};

function calculate_position(string[] commands) returns Position {
    return commands.reduce(
        function(Position position, string command) returns Position {

        string[] command_parts = regex:split(command, " ");
        string direction = command_parts[0];
        int value = checkpanic int:fromString(command_parts[1]);

        if (direction == "forward") {
            position.horizontal += value;
            position.depth += position.aim * value;
        } else if (direction == "up") {
            position.aim -= value;
        } else if (direction == "down") {
            position.aim += value;
        }

        return position;
    }, {
        horizontal: 0,
        depth: 0,
        aim: 0
    });
}

public function main() {
    io:ReadableByteChannel readableFieldResult = checkpanic io:openReadableFile("input.txt");
    io:ReadableCharacterChannel sourceChannel = new (readableFieldResult, "UTF-8");
    Position final_position = calculate_position(checkpanic sourceChannel.readAllLines());
    int result = final_position.horizontal * final_position.depth;
    io:println(result);
}

