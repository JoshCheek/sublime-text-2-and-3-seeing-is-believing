# Seeing Is Believing

Integration of `seeing_is_believing` to sublime text 2 as a plugin.

## Prerequisites

You need to have [`seeing_is_believing`](http://rubygems.org/gems/seeing_is_believing) installed:

```shell
gem install seeing_is_believing
```

## Installation

You have 2 options for installing SeeingIsBelieving Plugin: using Git, or just downloading it.

### Git

Open your terminal application and go to your Packages directory, whose location depends on your operating system:

* OS X

    ```shell
    cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages
    ```

* Linux

    ```shell
    cd ~/.Sublime\ Text 2/Packages/
    ```

* Windows

    ```shell
    cd %APPDATA%/Sublime Text 2/Packages/
    ```

After this, you just need to clone this repository:

```shell
git clone git://github.com/kassi/sublime-text-2-seeing-is-believing.git SeeingIsBelieving
```

### Download

Click on the nice cloud icon above and download the zip file containing this plugin.

Then unzip the file and move the resulting folder to your Packages directory.

## Usage

Open a ruby file write some code.

```ruby
10.times do |i|
  i * 2
end
```

Now run the command `Evaluate Ruby code with Seeing Is Believing` from your command pallete (⌘ + ⇧ + P on OS X).
Or press the pre-defined keyboard shortcut (⌥ + ⌘ + B on OS X). Watch your code getting annotated.

Now you want to edit it, so run `Remove Seeing Is Believing annotations`. Or press (⌥ + ⌘ + V on OS X)

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
