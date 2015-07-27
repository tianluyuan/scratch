fn main() {
    let mut my_num = 1i;
    my_num += 1;
    match my_num {
        a @ 0..2 => println!("{}", a),
        _ => println!("other")
    }
    println!("Hello world!");
}
