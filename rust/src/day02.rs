use crate::parser::parse_line_to_strings;

pub fn main() {
    let lines_as_string = parse_line_to_strings(2, true);
    let lines: Vec<_> = lines_as_string.lines().collect();
    for line in &lines {
        println!("{:?}", line)

    }
}