; ModuleID = "/Users/nampham/Documents/Theory_computation/codegen.py"
target triple = "x86_64-apple-darwin19.4.0"
target datalayout = ""

define void @"main"() 
{
entry:
  %".2" = add i8 10, 114
  %".3" = bitcast [5 x i8]* @"fstr" to i8*
  %".4" = call i32 (i8*, ...) @"printf"(i8* %".3", i8 %".2")
  ret void
}

declare i32 @"printf"(i8* %".1", ...) 

@"fstr" = internal constant [5 x i8] c"%i \0a\00"