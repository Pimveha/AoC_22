use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    let filename = "input";
    let file = File::open(filename).unwrap();
    let reader = BufReader::new(file);
    let mut score = 0;
    for (index, line) in reader.lines().enumerate() {

        let line = line.unwrap();
        let first_half = &line[0..line.len()/2];
        let last_half = &line[line.len()/2..];
        let abctrng = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
        let first_half_chars = first_half.chars();

        for c in first_half_chars {
            if last_half.contains(c){

                let char_val = abctrng.find(c);

                match char_val {
                    Some(val) => {
                        score += val;
                        println!("{}: {}", c, val);
                        println!("{}, {}|{}", index + 1, first_half, last_half);
                    }
                    None => {}
                }
                break;
            }
        }
    }
    println!("{}", score);
}

