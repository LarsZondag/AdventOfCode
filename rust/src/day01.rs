use crate::parser::parse_lines_to_ints;

pub fn main() {
    let arr = parse_lines_to_ints(1, false);

    part1(&arr);
    part2(&arr);
}

fn part1(arr: &Vec<i32>) {
    let mut increase = 0;
    for a in 0..arr.len() - 1 {
        if arr[a] < arr[a + 1] {
            increase += 1;
        }
    }
    println!("Answer to part 1: {}", increase)
}

fn part2(arr: &Vec<i32>) {
    let mut increase = 0;
    for i in 0..arr.len()-3 {
        if arr[i] < arr[i+3] {
            increase += 1;
        }
    }
    println!("Answer to part 2: {}", increase)
}
