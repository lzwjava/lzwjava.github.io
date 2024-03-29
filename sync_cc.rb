require 'pathname'
require 'fileutils'
require './sync_utils.rb'

base = '/Users/lzw/curiosity-courses'
target = Dir.pwd
posts_dir = File.join(target, '_posts', 'cc')
img_dir = File.join(target, 'assets', 'images', 'cc')

SyncUtils.mkdir!(posts_dir)
SyncUtils.mkdir!(img_dir)

dirs = Dir.glob(base + '/**').select { |x|
    File.directory? x
}

for dir in dirs
    pname = Pathname.new(dir)
    dir_name = pname.basename
    Dir.each_child(dir) { |x|
        if File.extname(x) == '.md'
            mdfile = File.join(dir, x)
            content = File.read(mdfile)
            if content.length == 0
                next
            end

            title = SyncUtils.extract_title(content)

            front = SyncUtils.post_front(title)
            
            content = content.lines[1..-1].join

            content = front + content

            ctime = File.birthtime(mdfile)
            date = ctime.strftime '%Y-%m-%d'
            file_name = date + '-' + x

            target_file = File.join(posts_dir, file_name)

            origin_img_dir = File.join(dir, 'img')        
            if Dir.exists?(origin_img_dir)
                target_img_dir = File.join(img_dir, dir_name)

                if !Dir.exists?(target_img_dir)
                    Dir.mkdir(target_img_dir)
                end               

                FileUtils.cp_r(origin_img_dir + '/.', target_img_dir)
            end

            img_path = "/assets/images/#{dir_name}/"

            content = content.gsub('./img/', img_path)

            File.write(target_file, content)
        end
    }
end
