#!/usr/bin/env ruby
puts ARGV[0].scan(/\[from:(\+?[[:alnum:]]*|[[:alnum:]]*)\] \[to:(\+?[[:alnum:]]*|[[:alnum:]]*)\] \[flags:(.*?)\]/).join(",")