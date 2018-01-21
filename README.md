# Seeing Is Believing

Integration of `seeing_is_believing` to Sublime Text 2 and 3.

## Prerequisites

You need to have [seeing\_is_believing](http://rubygems.org/gems/seeing_is_believing) 2.0 or greater installed:

```shell
gem install seeing_is_believing
```

## Installation

You have two options for installing the SeeingIsBelieving Plugin: using Git, or just downloading it. Then you will need to fix the settings.

**Git**

Open your terminal application and go to your Packages directory, whose location depends on your operating system:

Sublime Text 2:

* OS X - `cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages`
* Linux - `cd ~/.Sublime\ Text 2/Packages/`
* Windows - `cd %APPDATA%/Sublime Text 2/Packages/`

Sublime Text 3:

* OS X - `cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages`
* Linux - `cd ~/.Sublime\ Text 3/Packages/`
* Windows - `cd %APPDATA%/Sublime Text 3/Packages/`

After this, you need to clone this repository: `git clone git://github.com/JoshCheek/sublime-text-2-and-3-seeing-is-believing.git SeeingIsBelieving`

**Download**

Click on the nice cloud icon above and download the zip file containing this plugin. Then unzip the file and move the resulting folder to your Packages directory.

**Customizing**

You can customize which Ruby to use, and how to invoke SiB in the
[settings](https://github.com/JoshCheek/sublime-text-2-seeing-is-believing/blob/master/Seeing%20Is%20Believing.sublime-settings).

In particular, you'll need to go here if it can't find your Ruby.
In that situation, try opening a shell and running `ruby -e 'p RbConfig.ruby'`,
its possible that what it prints is the value you need to set. You can also
set environment variables here, and set any flags that you want passed to SiB.


## Usage

Open a Ruby file or write some code.

```ruby
10.times do |i|
  i * 2
end
```

Now run the command `Evaluate Ruby code with Seeing Is Believing` from your command pallete (⌘ + ⇧ + P on OS X) or press the pre-defined keyboard shortcut (⌥ + ⌘ + B on OS X).
You will see comments added adjacent to each line of your code, showing you what that line evaluated to.

```ruby
10.times do |i|
  i * 2          # => 0, 2, 4, 6, 8, 10, 12, 14, 16, 18
end              # => 10
```

Now you want to edit it, so run `Remove Seeing Is Believing annotations` or press (⌥ + ⌘ + V on OS X).
And you are back to the original.

There are also some default snippets you can use to play around with SiB.

* `s_arb` tab        - In memory ActiveRecord environment
* `s_nokogiri` tab   - Practice parsing html/xml/css selectors/xpath in Ruby
* `s_sinatra` tab    - Play with Sinatra, without needing to host it on a server
* `s_reflection` tab - Examples of reflection in Ruby (knowing these makes SiB much more useful)


## Configuration

You can edit these from your preferences folder. You can specify how to find Ruby (e.g. integrate with your version manager).
And you can specify what command-line arguments to pass to Seeing Is Believing. I'm trying to figure out how to get this in the menu,
but the docs are pretty weak.

## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request

## Author

Karsten Silkenbäumer wrote the one for XMPfilter that I (Josh Cheek) modified to work with Seeing Is Believing.
