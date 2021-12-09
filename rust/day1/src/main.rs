use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    let f = BufReader::new(File::open("input.txt").unwrap());

    let arr: Vec<u16> = f.lines().map(|l| l.unwrap().parse().unwrap()).collect();

    part1(&arr);
    part2(&arr);
}

fn part1(arr: &Vec<u16>) {
    let mut increase = 0;
    for a in 0..arr.len() - 1 {
        if arr[a] < arr[a + 1] {
            increase += 1;
        }
    }
    println!("Answer to part 1: {}", increase)
}

fn part2(arr: &Vec<u16>) {
    let mut increase = 0;
    for i in 0..arr.len()-3 {
        if arr[i] < arr[i+3] {
            increase += 1;
        }
    }
    println!("Answer to part 2: {}", increase)
}
