# Seeing Is Believing

Integration of `seeing_is_believing` to sublime text 2 as a plugin.

## Prerequisites

You need to have [seeing_is_believing](http://rubygems.org/gems/seeing_is_believing) installed:

```shell
gem install seeing_is_believing
```

## Installation

You have 2 options for installing SeeingIsBelieving Plugin: using Git, or just downloading it. Then you will need to fix the settings.

**Git**

Open your terminal application and go to your Packages directory, whose location depends on your operating system:

* OS X `cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages`
* Linux `cd ~/.Sublime\ Text 2/Packages/`
* Windows `cd %APPDATA%/Sublime Text 2/Packages/`

After this, you need to clone this repository: `git clone git://github.com/JoshCheek/sublime-text-2-seeing-is-believing.git SeeingIsBelieving`

**Download**

Click on the nice cloud icon above and download the zip file containing this plugin. Then unzip the file and move the resulting folder to your Packages directory.

**Fixing Settings**

You will need ot update the [settings](https://github.com/JoshCheek/sublime-text-2-seeing-is-believing/blob/master/Seeing%20Is%20Believing.sublime-settings)
that tell this plugin how to run the code. This is in your package directory.

If you are using **rbenv**, you should only have to edit the environment variable specifying the `RBENV_VERSION`, you can see a list of possible values with `rbenv versions`.

If you are using **rvm**, make a wrapper for sublime (instructions are in the [textmate integration](https://rvm.io/integration/textmate/) section,
make the wrapper the same way they do for textmate, except name it sublime instead),
find the path with `which sublime_ruby`, and set that as the value of `ruby_command` in the settings file.

If you are using something else, you just need to make sure that `ruby_command` points to a 1.9+ version of Ruby that has `seeing_is_believing` installed.


## Usage

Open a ruby file write some code.

```ruby
10.times do |i|
  i * 2
end
```

Now run the command `Evaluate Ruby code with Seeing Is Believing` from your command pallete (⌘ + ⇧ + P on OS X).
Or press the pre-defined keyboard shortcut (⌥ + ⌘ + B on OS X).
You will see comments added adjacent to each line of your code, showing you what that line evaluated to.

```ruby
10.times do |i|
  i * 2          # => 0, 2, 4, 6, 8, 10, 12, 14, 16, 18
end              # => 10
```

Now you want to edit it, so run `Remove Seeing Is Believing annotations` or press (⌥ + ⌘ + V on OS X).
And you are back to the original.

## Configuration

You can edit these from your preferences folder. You can specify how to find Ruby (e.g. integrate with your version manager).
And you can specify what command-line arguments to pass to Seeing Is Believing. Trying to figure out how to get this in the menu,
but the docs are pretty weak.

## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request

## Author

Karsten Silkenbäumer wrote the one for XMPfilter that I (Josh Cheek) modified to work with Seeing Is Believing.
