use std::fs;

pub fn parse_lines_to_ints(day: u32, true_input: bool) -> Vec<i32> {
    parse_line_to_strings(day, true_input)
        .split_whitespace()
        .map(|el| el.parse::<i32>().unwrap())
        .collect()
}

pub fn parse_line_to_strings(day: u32, true_input: bool) -> String {
    let path;
    if true_input {
        path = format!("inputs/{:02}/input.txt", day);
    } else {
        path = format!("inputs/{:02}/sample.txt", day);
    }
    println!("{}", path);
    let output = fs::read_to_string(&path)
        .expect(&*format!("Could not find {}", path)).to_owned();
    return output;
}