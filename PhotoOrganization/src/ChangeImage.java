import java.awt.BorderLayout;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
 
import javax.imageio.ImageIO;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;

import org.python.util.PythonInterpreter;

 
public class ChangeImage extends JFrame implements ActionListener {
    //멤버변수
    private BufferedImage pic;
    private JButton btn1, btn2, btn3;
    private JPanel imgPanel;
    
    private static PythonInterpreter interpreter;
    
    public void renameFile(String filename, String newFilename) {
        File file = new File( filename );
        File fileNew = new File( newFilename );
        if( file.exists() ) file.renameTo( fileNew );
    }

   
    //생성자
    public ChangeImage() {
        setTitle("File name changer");
        setSize(200, 330);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
       
        imgPanel = new ChangeImagePanel();
        try {
            pic = ImageIO.read(new File("C:\\Java\\mcw_1.png"));
        } catch (IOException e) {
            // TODO Auto-generated catch block
            System.out.println("이미지 없음!");
        }
        JPanel panel = new JPanel();
        panel.setLayout(new GridLayout(1, 2));
        panel.add(btn1 = new JButton("Get picture"));
        btn1.addActionListener(this);
        panel.add(btn2 = new JButton("Get Info"));
        btn2.addActionListener(this);
        panel.add(btn3 = new JButton("Change File name"));
        btn3.addActionListener(this);

       
        add(imgPanel, BorderLayout.CENTER);
        add(panel, BorderLayout.SOUTH);
        pack();
        setVisible(true);
    }
   
    class ChangeImagePanel extends JPanel {
        public ChangeImagePanel() {
        }
       
        @Override
        public void paint(Graphics g) {
            g.drawImage(pic, 0, 0, null);
        }
       
        @Override
        public Dimension getPreferredSize() {
            if (pic == null) {
                return new Dimension(640, 640);
            } else {
                return new Dimension(pic.getWidth(), pic.getHeight());
            }
        }
    }
   
    //멤버메소드
    @Override
    public void actionPerformed(ActionEvent e) {
        String imgFile = "";
        String path = "C:\\Users\\pmcsp\\eclipse-workspace\\Final\\test_img\\";
        if (e.getSource() == btn1) 
        {
            imgFile = "img1.JPG";
            
            try {
                pic = ImageIO.read(new File( path + imgFile));
            } catch (IOException e1) {
                // TODO Auto-generated catch block
                System.out.println("이미지 없음!");
            }	
            
          
        } else if(e.getSource() == btn2) 
        {
        	
            interpreter = new PythonInterpreter();
            System.out.println("import setting..!");

           // interpreter.exec("from PIL import Image");
            System.out.println("Run Python program..!	");

            interpreter.execfile("Get_Metadata.py");
    	
        	/*
        	try {
				Process p = Runtime.getRuntime().exec("python C:\\Users\\pmcsp\\eclipse-workspace\\Final\\src\\Get_Metadata.py");
				
			} catch (IOException e1) {
				// TODO Auto-generated catch block
				e1.printStackTrace();
			}
        	*/

        	
        }
        else
        {
            imgFile = "img1.JPG";

            try {
                pic = ImageIO.read(new File(path + imgFile));
            } catch (IOException e1) {
                // TODO Auto-generated catch block
                System.out.println("Cannot Find Image!");
            }	

        	renameFile(path + imgFile, path + "Flower.jpg");
        	System.out.println("button 3 is clicked");
        }

       
        imgPanel.repaint();
    }
    
    public static void main(String[] args) {
        new ChangeImage();
    }
}