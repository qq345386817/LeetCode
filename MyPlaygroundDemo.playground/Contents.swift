//: Playground - noun: a place where people can play

import UIKit

var str = "Hello, World"
print(str.applyingTransform(StringTransform.latinToThai, reverse: false)!)
print(str.applyingTransform(StringTransform.latinToGreek, reverse: false)!)
print(str.applyingTransform(StringTransform.latinToArabic, reverse: false)!)
print(str.applyingTransform(StringTransform.latinToHangul, reverse: false)!)
print(str.applyingTransform(StringTransform.latinToHebrew, reverse: false)!)
print(str.applyingTransform(StringTransform.latinToCyrillic, reverse: false)!)
print(str.applyingTransform(StringTransform.latinToHiragana, reverse: false)!)
print(str.applyingTransform(StringTransform.latinToKatakana, reverse: false)!)
var str2 = "你好，世界"
str2.applyingTransform(StringTransform.mandarinToLatin, reverse: false)
