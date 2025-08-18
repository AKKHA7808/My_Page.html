from django.core.management.base import BaseCommand
from main.models import Skill, Project, SiteConfiguration

class Command(BaseCommand):
    help = 'Create sample data for the portfolio'

    def handle(self, *args, **options):
        self.stdout.write('🎯 Creating sample portfolio data...')
        
        # Create sample skills
        skills_data = [
            {'name': 'Python', 'proficiency': 90, 'category': 'backend', 'icon': 'fab fa-python', 'is_featured': True, 'order': 1},
            {'name': 'Django', 'proficiency': 85, 'category': 'backend', 'icon': 'fab fa-python', 'is_featured': True, 'order': 2},
            {'name': 'JavaScript', 'proficiency': 80, 'category': 'frontend', 'icon': 'fab fa-js-square', 'is_featured': True, 'order': 3},
            {'name': 'HTML5', 'proficiency': 95, 'category': 'frontend', 'icon': 'fab fa-html5', 'is_featured': True, 'order': 4},
            {'name': 'CSS3', 'proficiency': 90, 'category': 'frontend', 'icon': 'fab fa-css3-alt', 'is_featured': True, 'order': 5},
            {'name': 'Bootstrap', 'proficiency': 85, 'category': 'frontend', 'icon': 'fab fa-bootstrap', 'is_featured': False, 'order': 6},
            {'name': 'PostgreSQL', 'proficiency': 75, 'category': 'database', 'icon': 'fas fa-database', 'is_featured': False, 'order': 7},
            {'name': 'Git', 'proficiency': 80, 'category': 'devops', 'icon': 'fab fa-git-alt', 'is_featured': False, 'order': 8},
        ]
        
        for skill_data in skills_data:
            skill, created = Skill.objects.get_or_create(
                name=skill_data['name'],
                defaults=skill_data
            )
            if created:
                self.stdout.write(f'✅ Created skill: {skill.name}')
            else:
                self.stdout.write(f'⚠️  Skill already exists: {skill.name}')
        
        # Create sample projects
        projects_data = [
            {
                'title': 'Django Portfolio Website',
                'short_description': 'เว็บไซต์ portfolio ส่วนตัวที่สร้างด้วย Django และ Bootstrap',
                'description': 'เว็บไซต์ portfolio ส่วนตัวที่แสดงผลงาน ทักษะ และข้อมูลติดต่อ พัฒนาด้วย Django framework และใช้ Bootstrap 5 สำหรับ responsive design มีระบบ admin สำหรับจัดการเนื้อหา',
                'github_url': 'https://github.com/username/portfolio',
                'demo_url': 'https://portfolio.vercel.app',
                'is_featured': True,
                'order': 1,
            },
            {
                'title': 'Task Management System',
                'short_description': 'ระบบจัดการงานสำหรับทีม พัฒนาด้วย Django',
                'description': 'ระบบจัดการงานที่ช่วยให้ทีมสามารถติดตามความคืบหน้าของโปรเจค มีฟีเจอร์การแจ้งเตือน การมอบหมายงาน และรายงานผล',
                'github_url': 'https://github.com/username/task-management',
                'demo_url': '',
                'is_featured': True,
                'order': 2,
            },
            {
                'title': 'E-commerce API',
                'short_description': 'REST API สำหรับระบบอีคอมเมิร์ซ',
                'description': 'REST API ที่สมบูรณ์สำหรับระบบอีคอมเมิร์ซ มีระบบการจัดการสินค้า คำสั่งซื้อ ระบบชำระเงิน และระบบผู้ใช้งาน',
                'github_url': 'https://github.com/username/ecommerce-api',
                'demo_url': '',
                'is_featured': False,
                'order': 3,
            },
        ]
        
        for project_data in projects_data:
            project, created = Project.objects.get_or_create(
                title=project_data['title'],
                defaults=project_data
            )
            if created:
                # Add some technologies to the project
                python_skill = Skill.objects.filter(name='Python').first()
                django_skill = Skill.objects.filter(name='Django').first()
                if python_skill:
                    project.technologies.add(python_skill)
                if django_skill:
                    project.technologies.add(django_skill)
                
                self.stdout.write(f'✅ Created project: {project.title}')
            else:
                self.stdout.write(f'⚠️  Project already exists: {project.title}')
        
        # Create site configuration
        site_config, created = SiteConfiguration.objects.get_or_create(
            id=1,
            defaults={
                'site_title': 'My Portfolio',
                'site_subtitle': 'Full Stack Developer & Creative Thinker',
                'about_text': '''สวัสดีครับ! ผมเป็น Full Stack Developer ที่มีความหลงใหลในการพัฒนาเว็บแอปพลิเคชัน 
                
ผมมีประสบการณ์ในการทำงานกับเทคโนโลยีต่างๆ ทั้ง Frontend และ Backend รวมถึงการออกแบบ Database และ API

ความสนใจของผม:
• การพัฒนาเว็บแอปพลิเคชันที่มีประสิทธิภาพ
• การเรียนรู้เทคโนโลยีใหม่ๆ
• การแก้ปัญหาที่ซับซ้อน
• การสร้างประสบการณ์ผู้ใช้ที่ดี

ผมพร้อมที่จะร่วมงานกับทีมในการสร้างโซลูชันที่มีคุณภาพและตอบโจทย์ผู้ใช้งาน''',
                'contact_email': 'your.email@example.com',
                'contact_phone': '+66 xx xxx xxxx',
                'github_url': 'https://github.com/yourusername',
                'linkedin_url': 'https://linkedin.com/in/yourusername',
                'facebook_url': 'https://facebook.com/yourusername',
                'twitter_url': 'https://twitter.com/yourusername',
            }
        )
        
        if created:
            self.stdout.write('✅ Created site configuration')
        else:
            self.stdout.write('⚠️  Site configuration already exists')
        
        self.stdout.write('\n🎉 Sample data creation completed!')
        self.stdout.write('💡 You can now:')
        self.stdout.write('   - Visit /admin/ to manage your content')
        self.stdout.write('   - Edit the sample data as needed')
        self.stdout.write('   - Add your own projects and skills')
