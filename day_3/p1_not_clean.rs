use std::fs::File;
use std::io::{BufRead, BufReader};
// use array_append::push;

fn print_type_of<T>(_: &T) {
    println!("{}", std::any::type_name::<T>())
}

fn main() {
    // let filename = "src/main.rs";
    let filename = "input";
    // Open the file in read-only mode (ignoring errors).
    let file = File::open(filename).unwrap();
    let reader = BufReader::new(file);

    // Read the file line by line using the lines() iterator from std::io::BufRead.
    for (index, line) in reader.lines().enumerate() {
        let line = line.unwrap(); // Ignore errors.
        // Show the line and its number.
        let first_half = &line[0..line.len()/2];
        let last_half = &line[line.len()/2..];
        // println!("{}. {}", index + 1, line);
        // println!("   {}-{}", first_half, last_half);
        let abctrng = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
        let first_half_chars = first_half.chars();
        // let mut ar: [i8; 8] = [0; 8];
        // println!("{:?}", ar);
        for c in first_half_chars {
        	if last_half.contains(c){
        		// let char_val = abctrng.find(c);
        		// let Some(char_val) = abctrng.find(c);
        		let char_val = abctrng.find(c);
        		match char_val {
        			Some(val) => {
        				print_type_of(&val);
        				print_type_of(&score);
        				// .parse::<i32>().unwrap();
        				// let org_score = score;
        				// let mut score = org_score + val;
        				score += val;
        				// println!("{:?}", val + score);
        				// println!("{:?}", val);
        				// ar[index] = val
        				println!("{:?}", score + val);
        				println!("{}, {}: {}|{}", index + 1, c, first_half, last_half);
        			}
        			None => {}
        		}
        		// if let Some(x) = abctrng.find(c){
        			// println!("{}, {}: {}|{} value: {:?}", index + 1, c, first_half, last_half, char_val);
        		// 	score = score + char_val;
        		// println!("{}, {}: {}|{} value: {:?}", index + 1, c, first_half, last_half, char_val);
        		// score = score + char_val;
        		break;
        	}
        }
    }
}


// If you encounter this error you probably need to use a `match` or `if let` to
// deal with the possibility of failure. Example:

// ```
// let x = Some(1);

// match x {
//     Some(y) => {
//         // do something
//     },
//     None => {}
// }

// // or:

// if let Some(y) = x {
//     // do something
// }